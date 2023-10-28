from concurrent import futures

import grpc

from proto import image_pb2_grpc, image_pb2


class ImageProcessingService(image_pb2_grpc.ImageProcessingServiceServicer):
    def ProcessImage(self, request_iterator, context):
        for request in request_iterator:
            image = request.image

            print(f'received {len(image)}')

            yield image_pb2.ImageResponse(index=request.index, image_with_contour=image, recognition_result='123456',
                                          metric=1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_pb2_grpc.add_ImageProcessingServiceServicer_to_server(ImageProcessingService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()