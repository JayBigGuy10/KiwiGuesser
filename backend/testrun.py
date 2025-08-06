import rasterio
from rasterio.windows import from_bounds
from rasterio.session import AWSSession
import boto3
import matplotlib.pyplot as plt

# COG location in S3
s3_url = "s3://nz-imagery/waikato/waikato_2021_0.1m/rgb/2193/BB32_1000_4347.tiff"

# BBOX from JSON (in WGS84)
bbox_wgs84 = [175.0069028, -37.2181507, 175.0124815, -37.2115728]

# Set up AWS session (public S3 buckets often don't need creds)
session = boto3.Session()
aws_session = AWSSession(session)

# Open the COG using Rasterio
with rasterio.Env(aws_session):
    with rasterio.open(s3_url) as src:
        # Reproject WGS84 bbox to image CRS (2193 - NZTM2000)
        from rasterio.warp import transform_bounds
        bbox = transform_bounds('EPSG:4326', src.crs, *bbox_wgs84, densify_pts=21)

        # Create window from bounds
        window = from_bounds(*bbox, transform=src.transform).round_offsets().round_lengths()
        data = src.read(window=window)
        transform = rasterio.windows.transform(window, src.transform)

        # Plot using matplotlib
        fig, ax = plt.subplots(figsize=(10, 10))
        if data.shape[0] == 3:  # RGB
            img = data.transpose((1, 2, 0))
            ax.imshow(img)
        else:
            ax.imshow(data[0], cmap='gray')
        ax.set_title("Rendered Bounding Box")
        ax.axis('off')
        plt.show()
