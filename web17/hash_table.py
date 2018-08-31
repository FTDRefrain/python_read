# 使用 timeit 测量时间
# 来对比 hashtable 和 list 的存取时间


class HashTable(object):
    def __init__(self):
        # table 是用来存储数据的数组
        # 先让它有 10007 个格子好了
        # 上课的时候说过, 这个尺寸最好选素数
        # 这样可以得到更为合理的下标分布
        self.table_size = 10007
        self.table = [0] * self.table_size

    # 这个魔法方法是用来实现 in  not in 语法的
    def __contains__(self, item):
        return self.has_key(item)
        
    def has_key(self, key):
        """
        检查一个 key 是否存在, 时间很短, 是 O(1)
        如果用 list 来存储, 需要遍历, 时间是 O(n)
        """
        index = self._index(key)
        # 取元素
        v = self.table[index]
        if isinstance(v, list):
            # 检查是否包含我们要找的 key
            for kv in v:
                if kv[0] == key:
                    return True
        # 如果得到的是 int 0 说明没找到, 返回 False
        # 如果得到的是 list 但是遍历结果没有我们要找的 key 也是没找到
        return False

    def _insert_at_index(self, index, key, value):
        # 检查下标处是否是第一次插入数据
        v = self.table[index]
        data = [key, value]
        # 也可以用这个判断 if v == 0:
        if isinstance(v, int):
            # 如果是第一次, 得到的是 int 0
            # 那么就插入一个 list 来存, 以后相同 key 的元素都放这里面
            # 注意我们把 key value 作为一个数组保存进去了, 这是因为
            # 会出现相同 hash 值的 key
            # 这时候就需要比较原始信息来找到相应的数据
            self.table[index] = [data]
        else:
            # 如果不是, 得到的会是 list, 直接 append
            self.table[index].append(data)

    def add(self, key, value):
        """
        add 函数往 hashtable 中加入一对元素
        我们先只支持字符串当 key
        """
        # 先计算出下标
        index = self._index(key)
        # 在下标处插入元素
        self._insert_at_index(index, key, value)

    def get(self, key, default_value=None):
        """
        这个和 dict 的 get 函数一样
        """
        index = self._index(key)
        # 取元素
        v = self.table[index]
        if isinstance(v, list):
            # 检查是否包含我们要找的 key
            for kv in v:
                if kv[0] == key:
                    return kv[1]
        # 如果得到的是 int 0 说明没找到, 返回 default_value
        # 如果得到的是 list 但是遍历结果没有我们要找的 key 也是没找到
        return default_value

    def _index(self, key):
        # 先计算出下标
        return self._hash(key) % self.table_size

    def _hash(self, s):
        """
        下划线开始的函数被我们视为私有函数
        但实际上还是可以在外部调用, 这只是一个给自己看的标记
        """
        n = 1
        f = 1
        for i in s:
            n += ord(i) * f
            f *= 10
        return n


def test():
    import uuid
    names = [
        'gua',
        'xiao',
        'name',
        'web',
        'python',
    ]
    ht = HashTable()
    for key in names:
        value = uuid.uuid4()
        ht.add(key, value)
        print('add 元素', key, value)
    for key in names:
        v = ht.get(key)
        print('get 元素', key, v)
    print('魔法方法', 'gua' in ht)


if __name__ == '__main__':
    test()
