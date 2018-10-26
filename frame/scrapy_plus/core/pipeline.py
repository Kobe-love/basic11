class Pipeline(object):
    def process_item(self, item):
        print("管道.{}".format(item.data))
        return item