import json

base_long = 2.1128503573367112
base_lat = 41.39271869720619


def create_deliveries():
    print("creating_deliveries...")
    deliveries = []
    for index in range(1, 51):
        delivery = {
            "id": index,
            "address": "Address {}".format(index),
            "latitude": base_lat + index * 0.0001,
            "longitude": base_long + index * 0.001,
            "customer": "Customer {}".format(index)
        }
        deliveries.append(delivery)
    print(json.dumps(deliveries))


if __name__ == "__main__":
    create_deliveries()