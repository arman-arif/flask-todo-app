from app.routes import blueprint


class Route:

    @staticmethod
    def get(path: str, action) -> None:
        blueprint.add_url_rule(path, view_func=action, methods=['GET'])

    @staticmethod
    def post(path: str, action) -> None:
        blueprint.add_url_rule(path, view_func=action, methods=['POST'])

    @staticmethod
    def delete(path: str, action) -> None:
        blueprint.add_url_rule(path, view_func=action, methods=['DELETE'])

    @staticmethod
    def put(path: str, action) -> None:
        blueprint.add_url_rule(path, view_func=action, methods=['PUT', 'PATCH'])

    @staticmethod
    def blueprint():
        return blueprint
