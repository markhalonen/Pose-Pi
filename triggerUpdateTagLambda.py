import boto3
import config
client = boto3.client('sns')

def triggerUpdateTag():
	response = client.publish(
		TopicArn='arn:aws:sns:us-east-1:815393274756:InvokeUpdateTagLambda',
		Subject='UpdateHardwareTag',
		Message=config.readId(),
		MessageAttributes={
			'string' : {
				'DataType' : 'String',
				'StringValue' : 'string'
				}
		})






