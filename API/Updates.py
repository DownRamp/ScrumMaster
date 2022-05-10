from query import updates

class Updates:
    def get(self):
        global cur
        updates.get_updates(cur)

    def post(self):
        global cur
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('userId', required=True)  # add args
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        new_data = pd.DataFrame({
            'userId': args['userId'],
            'name': args['name'],
            'city': args['city'],
            'locations': [[]]
        })
        # Create a 2 week sprint
        # Trigger check ins
        # Handel incoming requests Start API
        # Check and store velocity
        updates.save_updates(cur, new_data)