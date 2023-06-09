.PHONY = deploy
stack-name = ccm-sam-lambda-dev
capabilities = CAPABILITY_IAM
bucket = ccm-sam-lambda-dev
s3prefix = builds
region = us-east-1
directory = .aws-sam

deploy: | $(directory)
	sam build
	sam deploy \
	--stack-name ${stack-name} \
	--resolve-image-repos \
	--s3-bucket ${bucket} \
	--region ${region} \
	--capabilities CAPABILITY_IAM


