from route4me import Route4Me

KEY = "11111111111111111111111111111111"


def main():
    r4m = Route4Me(KEY)
    route = r4m.route
    response = route.get_routes(limit=10, Offset=5)
    if hasattr(response, 'errors'):
        print('. '.join(response.errors))
    else:
        response = route.get_route(route_id=response[0].route_id)
        if hasattr(response, 'errors'):
            print('. '.join(response.errors))
        else:
            print('Route ID: {}'.format(response.route_id))
            route_destination_id = response.addresses[1].route_destination_id
            route_destination_id2 = response.addresses[2].route_destination_id
            data = {
                "route_destination_id": route_destination_id,
                "route_id": response.route_id,
                "addresses": [{
                    "route_destination_id": route_destination_id2,
                    "sequence_no": 2,
                }]
            }
            response = route.resequence_route(**data)
            print('Optimization Problem ID: {}'.format(
                response.optimization_problem_id))
            print('Route ID: {}'.format(response.route_id))
            for i, address in enumerate(response.addresses):
                print('Address #{}'.format(i))
                print('\tAddress: {0}'.format(address.address))
                print('\tRoute Destination ID: {0}'.format(
                    address.route_destination_id))


if __name__ == '__main__':
    main()
