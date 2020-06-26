def memo(f):
    cache = {}
    were_lists = set()

    def wrapped_func(*args):
        new_args = []
        for i, arg in enumerate(args):
            if isinstance(arg, list):
                were_lists.add(i)
                new_args.append(tuple(arg))
            else:
                new_args.append(arg)

        args = tuple(new_args)

        if args in cache:
            return cache[args]

        if len(args) == 0:
            cache[args] = f()
        else:
            proper_args = []
            for i, arg in enumerate(args):
                if i in were_lists:
                    proper_args.append(list(arg))
                else:
                    proper_args.append(arg)

            cache[args] = f(*proper_args)

        return cache[args]

    return wrapped_func

