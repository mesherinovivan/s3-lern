import asyncio
import aiobotocore


async def main():

    session = aiobotocore.get_session()
    async with session.create_client(service_name='s3',
                      use_ssl=False, endpoint_url='http://localhost:7000',
                      aws_access_key_id='AKIAIOSFODNN7EXAMPLE', aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
                                     , region_name='us-west-2') as client:
        resp = await client.put_object(
            Bucket='test',
            Key='e1',
            Body='ddddddddddd'
        )

        response = await client.get_object(Bucket='test1', Key='e1')
        async with response['Body'] as stream:
            data = await stream.read()

            print(data)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()