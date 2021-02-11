
class TestApi:

    async def test_ping(self, client):
        resp = await client.get('api/ping')
        assert resp.status == 200
        resp_data = await resp.json()
        print(resp_data)
        assert resp_data['message'] == 'pong'
