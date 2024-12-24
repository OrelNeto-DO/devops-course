import boto3

# Create an EC2 client to interact with AWS EC2 service
ec2 = boto3.client('ec2')

# Get the list of all available AWS regions
response = ec2.describe_regions()

# Extract the region names from the response and store them in a list
regions = [region['RegionName'] for region in response['Regions']]

# Iterate through each region to fetch instances
for region in regions:
    print(f"Region: {region}")
    
    # Create a new EC2 client for the current region
    ec2_region = boto3.client('ec2', region_name=region)

    # Fetch the details of all EC2 instances in the current region
    instances = ec2_region.describe_instances()

    # Loop through the reservations and instances to display instance details
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            # Print the instance ID and its current state (e.g., running, stopped)
            print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
