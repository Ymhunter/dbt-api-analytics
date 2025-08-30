import dlt
import requests

ENDPOINTS = {
    "users": "Users",
    "products": "Products",
    "carts": "Carts"
}

@dlt.source
def dummyjson_source():
    for endpoint, description in ENDPOINTS.items():

        @dlt.resource(name=endpoint, write_disposition="replace")
        def fetch_resource():
            url = f"https://dummyjson.com/{endpoint}"
            response = requests.get(url)
            response.raise_for_status()
            json_data = response.json()

            if endpoint == "users":
                data = json_data.get("users", [])
            elif endpoint == "products":
                data = json_data.get("products", [])
            elif endpoint == "carts":
                data = json_data.get("carts", [])
            else:
                data = []

            for item in data:
                item["endpoint"] = endpoint
                item["description"] = description
                yield item

        yield fetch_resource

pipeline = dlt.pipeline(
    pipeline_name="dummyjson_pipeline",
    destination="duckdb",
    dataset_name="raw_dummyjson"
)

load_info = pipeline.run(dummyjson_source())
print(load_info)
