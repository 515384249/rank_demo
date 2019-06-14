def get_pagination_data(paginator, page_obj, count=20, around_count=1):
    """
    自定义的分页方法
    :param paginator:分页器
    :param page_obj:分页对象
    :param count:每页显示条数
    :param around_count:前后显示多少页，如当前为第5页，则只显示3、4、5、6、7。
    :return:
    """
    current_page = page_obj.number  # 获取当前对象的数量
    num_pages = paginator.num_pages  # 获取分页器的页数
    left_has_more = False  # 左边是否有更多
    right_has_more = False  # 右边是否还有更多
    if current_page <= around_count + 2:
        left_pages = range(1, current_page)  # 这里由于列表索引，需要对其进行增加操作
    else:
        left_has_more = True  # 逻辑写完有点忘了
        left_pages = range(current_page - around_count, current_page)
    if current_page >= num_pages - around_count - 1:
        right_pages = range(current_page + 1, num_pages + 1)
    else:
        right_has_more = True
        right_pages = range(current_page + 1, current_page + around_count + 1)
    try:
        count = int(count)  # 将传入的自定义每页条数转换成数字
    except:
        count = 20
    start_number = (current_page - 1) * count + 1  # 显示开始条数，如当前是第2页，每页显示20条，则这个值是21
    stop_number = current_page * count  # 显示结束条数，如当前是第2页，每页显示20条，则这个值是40
    # 将结果集返回
    return {
        'left_pages': left_pages,
        'right_pages': right_pages,
        'current_page': current_page,
        'left_has_more': left_has_more,
        'right_has_more': right_has_more,
        'num_pages': num_pages,
        'start_number': start_number,
        'stop_number': stop_number,
    }
