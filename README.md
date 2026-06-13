# AWS Lambda Image Thumbnail Generator

## Project Overview

This project automatically generates image thumbnails whenever an image is uploaded to an Amazon S3 bucket.

The solution uses AWS Lambda, Amazon S3, IAM, CloudWatch, and Pillow (Lambda Layer).

---

## AWS Services Used

- Amazon S3
- AWS Lambda
- IAM
- CloudWatch
- Lambda Layers (Pillow)

---

## Workflow

1. Upload image to Source S3 Bucket.
2. S3 Event triggers Lambda Function.
3. Lambda downloads image.
4. Pillow resizes image to fit within 200x200 pixels.
5. Thumbnail is stored in Output S3 Bucket.

---

## Lambda Function

```python
image.thumbnail((200,200))
```

---

## Screenshots

### Buckets
![Buckets](Screenshots/01-Buckets.png)

### Source Bucket
![Source-Bucket](Screenshots/02-Source-Bucket.png)

### Lambda Code

![Lambda-Code](Screenshots/03-Lambda-Code.png)

### S3 Trigger

![S3-Trigger](Screenshots/04-S3-Trigger.png)

### Pillow Layer

![Pillow-Layer](Screenshots/05-Pillow-Layer.png)

### Output Bucket

![Output-Bucket](Screenshots/06-Output-Bucket.png)

### Original-Img 

![Original-Img](Screenshots/07-Original-Img.png)

### Thumbnail-Img

![Thumbnail-Img](Screenshots/08-Thumbnail-Img.png)

---

## Result

Original Image:
- 1300 × 728
- 122.1 KB

Thumbnail Image:
- 200 × 112
- 4.4 KB

The thumbnail maintains the original aspect ratio while significantly reducing file size.

---

## Author

Prajwal