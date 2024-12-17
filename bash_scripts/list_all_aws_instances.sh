#!/bin/bash

regions=$(aws ec2 describe-regions --query "Regions[].RegionName" --output text)

echo "Fetching instances from all regions..."

for region in $regions; do
    echo "Region: $region"
    aws ec2 describe-instances \
        --region $region \
        --query "Reservations[].Instances[].[InstanceId, State.Name, InstanceType, PublicIpAddress]" \
        --output table
done
