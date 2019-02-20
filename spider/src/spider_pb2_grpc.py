# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import spider_pb2 as spider__pb2


class SpiderRpcStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SubmitRssFeed = channel.unary_unary(
        '/spiderrpc.SpiderRpc/SubmitRssFeed',
        request_serializer=spider__pb2.RssFeed.SerializeToString,
        response_deserializer=spider__pb2.SubmitResult.FromString,
        )
    self.SubmitBlogFeed = channel.unary_unary(
        '/spiderrpc.SpiderRpc/SubmitBlogFeed',
        request_serializer=spider__pb2.BlogFeed.SerializeToString,
        response_deserializer=spider__pb2.SubmitResult.FromString,
        )
    self.CrawlArticles = channel.unary_unary(
        '/spiderrpc.SpiderRpc/CrawlArticles',
        request_serializer=spider__pb2.SpiderList.SerializeToString,
        response_deserializer=spider__pb2.CrawlTaskResult.FromString,
        )


class SpiderRpcServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SubmitRssFeed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubmitBlogFeed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CrawlArticles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SpiderRpcServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SubmitRssFeed': grpc.unary_unary_rpc_method_handler(
          servicer.SubmitRssFeed,
          request_deserializer=spider__pb2.RssFeed.FromString,
          response_serializer=spider__pb2.SubmitResult.SerializeToString,
      ),
      'SubmitBlogFeed': grpc.unary_unary_rpc_method_handler(
          servicer.SubmitBlogFeed,
          request_deserializer=spider__pb2.BlogFeed.FromString,
          response_serializer=spider__pb2.SubmitResult.SerializeToString,
      ),
      'CrawlArticles': grpc.unary_unary_rpc_method_handler(
          servicer.CrawlArticles,
          request_deserializer=spider__pb2.SpiderList.FromString,
          response_serializer=spider__pb2.CrawlTaskResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'spiderrpc.SpiderRpc', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
