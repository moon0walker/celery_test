from celery import group, chain, chord
from proj.celery import app
from proj.tasks import add, mul, xsum, get_prime, error_handler


def canvas_test():
    try:
        print('=== celery.group ==')
        print( group( add.s(i) for i in range(25) )(10).get() )
        print()

        print('=== celery.chain ==')
        print( chain( add.s(4, 4), mul.s(2) )().get() )
        print()

        print('=== celery.chord ==')
        print(chord( (add.s(i, i) for i in range(25)), xsum.s() )().get())
        print()
    except Exception as err:
        print(str(err))


def link_test():
    print(add.apply_async( (4, 10), link=[mul.s(2), get_prime.s()], link_error=error_handler.s() ).get())


def primitives_test():
    # print(add.starmap([ (1, 2), (3, 4) ]).apply_async().get())

    # print(add.chunks(zip(range(1000), range(1000)), 10).apply_async().get())

    # res = (add.s(4, 2) | add.s(6))()
    # print(res.get())
    # print(res.parent.get())
    # print(res.parent.parent.get())

    # print( group(add.s(i, i) for i in range(10))().get() )

    # print( chord((add.s(i, i) for i in range(5)), xsum.s())().get() )

    # print( ( add.s(4, 4) | group(add.si(i, i) for i in range(10)) )().get() )

    # print( add.apply_async( (4, 10), link=[mul.s(2)], link_error=error_handler.s() ).get() )

    # res = (add.s(2, 4) | mul.s(10) | add.s(5)).apply_async()
    # print( list(res.collect()) )
    # print(res.parent.parent.graph)

    # print((add.s(2, 4) | mul.s(10) | add.s(5)).apply_async().get())
    # print((add.s(2, 4) | mul.s(10) | add.s(5))().get())

    print( chord( add.s(i, i) for i in range(10) )(xsum.s()).get() )


def shutdown_workers(control):
    print(control)
    # print('ping =>', control.ping())
    # print('shutdown =>', control.broadcast('shutdown'))
    # print('ping =>', control.ping())


def inspect_test():
    control = app.control
    inspect = control.inspect()
    print('registered =>', inspect.registered())
    print('active     =>', inspect.active())
    print('scheduled  =>', inspect.scheduled())
    print('reserved   =>', inspect.reserved())

    shutdown_workers(control)

    control.enable_events()
    control.disable_events()

if __name__ == '__main__':
    # primitives_test()
    # canvas_test()
    # add.delay(10, 11)
    print(add.delay(10, 11).get())
    # mul.apply_async( (10, 11), queue='broadcast' )
