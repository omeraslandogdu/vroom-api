import numpy as np
import vroom


class VRoomService:
    def __init__(self, data):
        self.data = data
        self.problem_instance = self.create_problem_instance()
        self.vehicle_ids = self.get_vehicle_ids()
        self.solution = self.solve_problem_instance(self.problem_instance)
        self.routes = self.reformat_routes(self.solution.routes, self.vehicle_ids)

    def create_problem_instance(self):
        problem_instance = vroom.Input()
        problem_instance.add_vehicle([vroom.Vehicle(id=vehicle.get("id"),
                                                    start=vehicle.get("start_index"),
                                                    capacity=vehicle.get("capacity")) for vehicle in
                                      self.data.get("vehicles", [])])
        problem_instance.add_job([vroom.Job(id=job.get("id"), location=job.get("location_index"),
                                            delivery=job.get("delivery"), service=job.get("service")) for job in
                                  self.data.get("jobs", [])]),

        problem_instance.set_durations_matrix(profile="car", matrix_input=self.data.get("matrix", []))

        return problem_instance

    def solve_problem_instance(self, problem_instance):
        solution = problem_instance.solve(exploration_level=5, nb_threads=4)

        return solution

    def reformat_solution(self, solution):
        response = {
            "total_delivery_duration": solution.summary.duration,
            "routes": self.routes
        }

        return response

    def reformat_routes(self, routes, vehicle_ids):
        response = {}

        for vehicle_id in vehicle_ids:
            df = routes.loc[(routes.vehicle_id == vehicle_id) & (routes.id != np.NAN)]
            route_data = {
                "jobs": df.id.values.astype(str).tolist(),
            }

            response[vehicle_id] = route_data

        return response

    def get_vehicle_ids(self):
        vehicles = self.data.get("vehicles", [])
        vehicle_ids = [vehicle.get("id") for vehicle in vehicles]

        return vehicle_ids

    def get_solution(self):
        solution = self.solve_problem_instance(self.problem_instance)
        response = self.reformat_solution(solution)

        return response
