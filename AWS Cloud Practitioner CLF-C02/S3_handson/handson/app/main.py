from fastapi import FastAPI, UploadFile, File, HTTPException
import boto3
import os
from botocore.exceptions import NoCredentialsError, ClientError
from app.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, BUCKET_NAME
from app.multipart_upload import upload_with_default_configuration
from app.copy_object_to_other_bucket import ObjectWrapper
app = FastAPI()

# S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# S3 resource for Object operations
s3_resource = boto3.resource(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # find file size
        file.file.seek(0, 2)
        file_size_bytes = file.file.tell()
        file.file.seek(0)
        file_size_mb = file_size_bytes / (1024 * 1024)

        # call updated function
        result = upload_with_default_configuration(
            file.file, BUCKET_NAME, file.filename, file_size_mb
        )

        return {"message": f"File '{file.filename}' uploaded successfully!", "results": result}

    except NoCredentialsError:
        raise HTTPException(status_code=403, detail="AWS credentials not found")
    except ClientError as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
    finally:
        await file.close()


@app.post("/copy/")
async def copy_file(source_key: str, dest_key: str, source_bucket: str = BUCKET_NAME, dest_bucket: str = BUCKET_NAME):
    """
    Copy an object from one location in S3 to another.
    """
    try:
        # Source and destination S3 objects
        source_obj = s3_resource.Object(source_bucket, source_key)
        dest_obj = s3_resource.Object(dest_bucket, dest_key)

        # Wrap source object
        wrapped_obj = ObjectWrapper(source_obj)
        wrapped_obj.copy(dest_obj)

        return {"message": f"File copied from '{source_bucket}/{source_key}' to '{dest_bucket}/{dest_key}' successfully!"}

    except ClientError as e:
        raise HTTPException(status_code=500, detail=f"Failed to copy object: {e}")

@app.delete("/delete/")
async def delete_file(key: str, bucket: str = BUCKET_NAME):
    """
    Delete an object from an S3 bucket.
    """
    try:
        obj = s3_resource.Object(bucket, key)
        obj.delete()
        return {"message": f"File '{key}' deleted from bucket '{bucket}' successfully!"}
    except ClientError as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete object: {e}")

@app.get("/generate_presigned_url/")
async def generate_presigned_url(key: str, bucket: str = BUCKET_NAME, expires_in: int = 60):
    """
    Generate a presigned URL to download a file from S3.
    """
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket, 'Key': key},
            ExpiresIn=expires_in
        )
        return {"url": url}
    except ClientError as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate presigned URL: {e}")
