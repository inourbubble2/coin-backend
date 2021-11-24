from flask_restx import reqparse


pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('page', type=int, required=False, default=1, help='Page number')
pagination_arguments.add_argument('per_page', type=int, required=False, choices=[2, 10, 20, 30, 40, 50, 100, 200],
                                  default=20, help='Results per page {error_msg}')

cafe_search_arguments = reqparse.RequestParser()
cafe_search_arguments.add_argument('name', type=str, required=False, help='Cafe Name')
cafe_search_arguments.add_argument('location', type=str, required=False, choices=['front', 'back', 'side', 'hoegi', ''],
                                   help='Cafe Location')

kakao_cafe_search_arguments = reqparse.RequestParser()
kakao_cafe_search_arguments.add_argument('name', type=str, required=True, help='Cafe Name')