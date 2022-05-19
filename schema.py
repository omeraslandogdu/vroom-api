ROUTING = {
    "type": "object",
    "properties": {
        "vehicles": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "number"
                    },
                    "start_index": {
                        "type": "number"
                    },
                    "capacity": {
                        "type": "array",
                        "items": {
                            "type": "number",
                        }
                    }
                }
            }
        },
        "jobs": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "number"
                    },
                    "location_index": {
                        "type": "number"
                    },
                    "delivery": {
                        "type": "array",
                        "items": {
                            "type": "number",
                        }
                    },
                    "service": {
                        "type": "number",
                    },
                }
            }
        },
        "matrix": {
            "type": "array",
            "items": {
                "type": "array",
                "items": {
                    "type": "number"
                }
            }
        }
    },
    "required": ["vehicles", "jobs", "matrix"]
}
