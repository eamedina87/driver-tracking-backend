import json

base_long = 2.1128503573367112
base_lat = 41.39271869720619


def create_deliveries():
    print("creating_deliveries...")
    deliveries = []
    for index in range(1, 31):
        delivery = {
            "id": index,
            "address": "Address {}".format(index),
            "latitude": base_lat + index * 0.0001,
            "longitude": base_long + index * 0.001,
            "customer_name": "Customer {}".format(index)
        }
        deliveries.append(delivery)
    obj = {
        "deliveries": {
            "deliveries": deliveries
        }
    }
    print(json.dumps(obj))


if __name__ == "__main__":
    create_deliveries()