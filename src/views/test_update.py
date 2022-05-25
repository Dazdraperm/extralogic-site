from src.json_rpc import JsonRPC

if __name__ == '__main__':
    json_rpc = JsonRPC()
    response = json_rpc.update_value_fields(value_fields=[{"id": 1, "value_field": "str"}])
