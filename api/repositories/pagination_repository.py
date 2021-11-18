def pagination(query, page, limit):
    total_items = query.count()
    item_count = query.offset((page - 1) * limit).limit(limit).count()
    total_pages = total_items // limit + 1

    return {
        'meta': {
            'item_count': item_count,
            'total_items': total_items,
            'items_per_page': limit,
            'total_pages': total_pages,
            'current_page': page,
        },
        'items': query.offset((page - 1) * limit).limit(limit).all()
    }


def pagination_with_link(query, page, limit, path):
    total_pages = query.count() // limit + 1
    paginated_value = pagination(query, page, limit)

    links = dict()
    links['self'] = {'href': f'https://uoslife.com/docs/{path}?page={page}&limit={limit}'}
    if page > 1:
        links['prev'] = {'href': f'https://uoslife.com/docs/{path}?page={page - 1}&limit={limit}'}
    if total_pages > page:
        links['next'] = {'href': f'https://uoslife.com/docs/{path}?page={page + 1}&limit={limit}'}

    paginated_value['_links'] = links
    return paginated_value

