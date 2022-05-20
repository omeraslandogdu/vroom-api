import json

import numpy as np
import vroom


def create_problem_instance(data):
    problem_instance = vroom.Input()
    problem_instance.add_vehicle([vroom.Vehicle(id=vehicle.get("id"),
                                                start=vehicle.get("start_index"),
                                                capacity=vehicle.get("capacity")) for vehicle in
                                  data.get("vehicles", [])])
    problem_instance.add_job([vroom.Job(id=job.get("id"), location=job.get("location_index"),
                                        delivery=job.get("delivery"), service=job.get("service")) for job in
                              data.get("jobs", [])]),

    problem_instance.set_durations_matrix(profile="car", matrix_input=data.get("matrix", []))

    return problem_instance


def solve_problem_instance(problem_instance):
    solution = problem_instance.solve(exploration_level=5, nb_threads=4)

    return solution


def reformat_solution(solution, vehicle_ids):
    response = {
        "total_delivery_duration": solution.summary.duration,
        "routes": reformat_routes(solution.routes, vehicle_ids)
    }

    return response


def reformat_routes(routes, vehicle_ids):
    response = {}

    for vehicle_id in vehicle_ids:
        df = routes.loc[(routes.vehicle_id == vehicle_id) & (routes.id != np.NAN)]
        route_data = {
            "jobs": df.id.values.tolist(),
        }

        response[vehicle_id] = route_data

    return response


def get_vehicle_ids(vehicles):
    vehicle_ids = [vehicle.get("id") for vehicle in vehicles]

    return vehicle_ids


def get_solution(data):
    problem_instance = create_problem_instance(data)
    solution = solve_problem_instance(problem_instance)
    response = reformat_solution(solution, get_vehicle_ids(data.get("vehicles", [])))

    return response
