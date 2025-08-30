import dlt
import requests

ENDPOINTS = {
    "users": "Users",
    "products": "Products",
    "categories": "Categories"
}

@dlt.source
def platzi_source():
    def make_resource(endpoint, description):
        @dlt.resource(name=endpoint, write_disposition="replace")
        def fetch_resource():
            url = f"https://api.escuelajs.co/api/v1/{endpoint}?offset=0&limit=100"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            for item in data:
                item["endpoint"] = endpoint
                item["description"] = description
                yield item

        return fetch_resource
    
    for endpoint, description in ENDPOINTS.items():
        yield make_resource(endpoint, description)


pipeline = dlt.pipeline(
    pipeline_name="platzi_pipeline",
    destination="duckdb",
    dataset_name="staging"
)

load_info = pipeline.run(platzi_source())
print(load_info)
