"""element :    [type -b, -p, -m, -e (1 letter)]
                [id [number for players and enemies (1)], [type for the different enemies (1)] (2)]
                [path]"""

levels = [
        #level 1-1
        ("f1",
        [["m00a1","m00a3","m00a5","b00b1","m00m1","e00e1","m00m1","b00b1","m00a1","m00a3","m00a5"],
        ["m00a2", "m00a4","m00a6","b00b1","b00b1","b00b1","b00b1","b00b1","m00a2","m00a4","m00a6"],
        ["b00b1", "b00b1","b00b1","m00m1","b00b1","m00m1","b00b1","m00m1","b00b1","b00b1","b00b1"],
        ["m00m1", "b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","m00m1"],
        ["b00b1", "b00b1","m00m1","b00b1","m00a1","m00a3","m00a5","b00b1","m00m1","b00b1","b00b1"],
        ["b00b1", "b00b1","m00m1","b00b1","m00a2","m00a4","m00a6","p00p1","m00m1","b00b1","b00b1"],
        ["m00m1", "b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","m00m1"],
        ["b00b1", "b00b1","b00b1","m00m1","b00b1","m00m1","b00b1","m00m1","b00b1","b00b1","b00b1"],
        ["m00a1", "m00a3","m00a5","b00b1","b00b1","b00b1","b00b1","b00b1","m00a1","m00a3","m00a5"],
        ["m00a2", "m00a4","m00a6","b00b1","m00m1","e10e1","m00m1","b00b1","m00a2","m00a4","m00a6"]]),


        #level 1-2
        ("f1",
        [["e00e1","b00b1","b00b1","b00b1","m00m1","b00b1","m00m1","b00b1","b00b1","b00b1","b00b1"],
        ["b00b1", "m00m1","m00m1","b00b1","m00m1","b00b1","m00m1","b00b1","m00m1","m00m1","b00b1"],
        ["b00b1", "m00m1","m00m1","b00b1","m00m1","b00b1","m00m1","b00b1","m00m1","m00m1","b00b1"],
        ["b00b1", "b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1"],
        ["m00m1", "m00m1","b00b1","m00m1","b00b1","m00m1","b00b1","m00m1","b00b1","m00m1","m00m1"],
        ["m00m1", "m00m1","b00b1","m00m1","b00b1","m00m1","p00p1","m00m1","b00b1","m00m1","m00m1"],
        ["b00b1", "b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1"],
        ["b00b1", "m00m1","m00m1","b00b1","m00m1","b00b1","m00m1","b00b1","m00m1","m00m1","b00b1"],
        ["b00b1", "m00m1","m00m1","b00b1","m00m1","b00b1","m00m1","b00b1","m00m1","m00m1","b00b1"],
        ["b00b1", "b00b1","b00b1","b00b1","m00m1","b00b1","m00m1","b00b1","b00b1","b00b1","e10e1"]]),


        #level 1-3
        ("f1",
        [["b00b1","b00b1","b00b1","m00m1","b00b1","m00m1","b00b1","m00m1","b00b1","m00m1","b00b1"],
        ["b00b1", "m00m1","e00e1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","m00m1","b00b1"],
        ["b00b1", "m00m1","b00b1","m00m1","b00b1","m00m1","b00b1","m00a1","m00a3","m00a5","b00b1"],
        ["b00b1", "m00a1","m00a3","m00a5","b00b1","b00b1","b00b1","m00a2","m00a4","m00a6","b00b1"],
        ["b00b1", "m00a2","m00a4","m00a6","b00b1","m00m1","p00p1","b00b1","b00b1","b00b1","b00b1"],
        ["b00b1", "b00b1","b00b1","b00b1","b00b1","b00b1","m00m1","b00b1","m00m1","m00m1","b00b1"],
        ["b00b1", "m00m1","e10e1","m00m1","b00b1","m00m1","b00b1","b00b1","b00b1","e20e1","m00m1"],
        ["b00b1", "b00b1","m00m1","b00b1","m00m1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1"],
        ["b00b1", "m00m1","m00m1","b00b1","m00m1","b00b1","m00a1","m00a3","m00a5","b00b1","b00b1"],
        ["b00b1", "m00m1","m00m1","b00b1","m00m1","b00b1","m00a2","m00a4","m00a6","b00b1","m00m1"],
        ["b00b1", "b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1","b00b1"]]),


        #level 2-1
        ("f2",
        [["e01e1","b00b2","b00b2","b00b2","b00b2","b00b2","b00b2","b00b2","b00b2","b00b2","e11e1"],
        ["b00b2", "b00b2","b00b2","b00b2","m00m2","b00b2","b00b2","b00b2","b00b2","b00b2","b00b2"],
        ["m00t1", "m00t3","m00t5","b00b2","b00b2","b00b2","m00m2","b00b2","m00t1","m00t3","m00t5"],
        ["m00t2", "m00t4","m00t6","b00b2","b00b2","b00b2","b00b2","b00b2","m00t2","m00t4","m00t6"],
        ["b00b2", "m00m2","b00b2","b00b2","m00t1","m00t3","m00t5","b00b2","b00b2","m00m2","m00m2"],
        ["b00b2", "b00b2","b00b2","b00b2","m00t2","m00t4","m00t6","b00b2","b00b2","b00b2","b00b2"],
        ["m00t1", "m00t3","m00t5","b00b2","b00b2","m00m2","b00b2","b00b2","m00t1","m00t3","m00t5"],
        ["m00t2", "m00t4","m00t6","b00b2","b00b2","b00b2","b00b2","b00b2","m00t2","m00t4","m00t6"],
        ["b00b2", "b00b2","m00m2","b00b2","b00b2","b00b2","b00b2","m00m2","b00b2","b00b2","b00b2"],
        ["e21e1", "b00b2","b00b2","b00b2","b00b2","p00p2","b00b2","b00b2","b00b2","b00b2","e31e1"]]),


        #level 2-2
        ("f2",
        [["e01e1","m00m2","m00m2","b00b2","m00m2","p00p2","m00m2","b00b2","m00m2","m00m2","b00b2"],
        ["b00b2", "b00b2","b00b2","b00b2","b00b2","b00b2","b00b2","b00b2","b00b2","b00b2","b00b2"],
        ["m00m2", "m00m2","b00b2","m00m2","m00m2","b00b2","m00m2","m00m2","e11e1","m00m2","m00m2"],
        ["b00b2", "b00b2","b00b2","b00b2","b00b2","m00m2","b00b2","b00b2","b00b2","b00b2","b00b2"],
        ["b00b2", "m00m2","m00m2","b00b2","m00m2","m00m2","b00b2","m00m2","m00m2","b00b2","m00m2"],
        ["e21e1", "m00m2","b00b2","b00b2","b00b2","b00b2","b00b2","b00b2","b00b2","b00b2","b00b2"],
        ["m00m2", "b00b2","m00m2","m00m2","b00b2","m00m2","m00m2","b00b2","m00m2","m00m2","b00b2"],
        ["b00b2", "b00b2","b00b2","b00b2","b00b2","b00b2","m00m2","b00b2","b00b2","m00m2","b00b2"],
        ["m00m2", "m00m2","b00b2","m00m2","m00m2","b00b2","m00m2","m00m2","b00b2","m00m2","m00m2"],
        ["e31e1", "b00b2","b00b2","m00m2","b00b2","b00b2","e41e1","m00m2","b00b2","b00b2","e51e1"]]),


        #level 2-3
        ("f2",
        [["b00b2","b00b2","b00b2","b00b2","m00t1","m00t3","m00t5","b00b2","b00b2","b00b2","b00b2"],
        ["b00b2", "e01e1","b00b2","b00b2","m00t2","m00t4","m00t6","b00b2","b00b2","e11e1","b00b2"],
        ["b00b2", "b00b2","b00b2","b00b2","m00t1","m00t3","m00t5","b00b2","b00b2","b00b2","b00b2"],
        ["b00b2", "b00b2","b00b2","b00b2","m00t2","m00t4","m00t6","b00b2","b00b2","b00b2","b00b2"],
        ["m00t1", "m00t3","m00t5","b00b2","b00b2","b00b2","b00b2","b00b2","m00t1","m00t3","m00t5"],
        ["m00t2", "m00t4","m00t6","b00b2","b00b2","p00p2","b00b2","b00b2","m00t2","m00t4","m00t6"],
        ["b00b2", "b00b2","b00b2","b00b2","m00t1","m00t3","m00t5","b00b2","b00b2","b00b2","b00b2"],
        ["b00b2", "b00b2","b00b2","b00b2","m00t2","m00t4","m00t6","b00b2","b00b2","b00b2","b00b2"],
        ["b00b2", "e21e1","b00b2","b00b2","m00t1","m00t3","m00t5","b00b2","b00b2","e31e1","b00b2"],
        ["b00b2", "b00b2","b00b2","b00b2","m00t2","m00t4","m00t6","b00b2","b00b2","b00b2","b00b2"]]),


        #level 3-1
        ("f3",
        [["v",   "v",    "v",    "v",    "m00m3","m00m3","m00m3","v",    "v",    "v",    "v"],
        ["v",    "v",    "m00m3","m00m3","e02e1","m00m5","b00b3","m00m3","m00m3","v",    "v"],
        ["v",    "m00m3","b00b3","m00m5","b00b3","b00b3","b00b3","b00b3","b00b3","m00m3","v"],
        ["v",    "m00m3","b00b3","b00b3","b00b3","m00m5","b00b3","m00m5","b00b3","m00m3","v"],
        ["m00m3","m00m5","b00b3","m00m5","b00b3","p00p3","b00b3","m00m5","b00b3","b00b3","m00m3"],
        ["m00m3","b00b3","b00b3","m00m5","b00b3","m00m5","b00b3","m00m5","m00m5","e12e1","m00m3"],
        ["v",    "m00m3","m00m5","b00b3","m00m5","b00b3","b00b3","b00b3","b00b3","m00m3","v"],
        ["v",    "m00m3","e22e1","b00b3","b00b3","m00m5","b00b3","m00m5","b00b3","m00m3","v"],
        ["v",    "v",    "m00m3","m00m3","b00b3","b00b3","b00b3","m00m3","m00m3","v",    "v"],
        ["v",    "v",   "v",     "v",    "m00m3","m00m3","m00m3","v",    "v",    "v",    "v"]]),


        #level 3-2
        ("f3",
        [["v",   "v",    "v",    "v",    "m00m3","m00m3","m00m3","v",    "v",    "v",    "v"],
        ["v",    "v",    "m00m3","m00m3","b00b3","e02e1","b00b3","m00m3","m00m3","v",    "v"],
        ["v",    "m00m3","b00b3","b00b3","b00b3","m00m5","b00b3","b00b3","b00b3","m00m3","v"],
        ["v",    "m00m3","b00b3","m00m5","m00m5","m00m5","m00m5","m00m5","b00b3","m00m3","v"],
        ["m00m3","e12e1","b00b3","b00b3","m00m5","p00p3","b00b3","b00b3","b00b3","e22e1","m00m3"],
        ["m00m3","e32e1","b00b3","b00b3","b00b3","b00b3","m00m5","b00b3","b00b3","e42e1","m00m3"],
        ["v",    "m00m3","b00b3","m00m5","m00m5","m00m5","m00m5","m00m5","b00b3","m00m3","v"],
        ["v",    "m00m3","b00b3","b00b3","b00b3","m00m5","b00b3","b00b3","b00b3","m00m3","v"],
        ["v",    "v",    "m00m3","m00m3","b00b3","e52e1","b00b3","m00m3","m00m3","v",    "v"],
        ["v",    "v",    "v",    "v",    "m00m3","m00m3","m00m3","v",    "v",    "v",    "v"]]),


        #level 3-3
        ("f3",
        [["v",   "v",    "v",    "v",    "m00m3","m00m3","m00m3","v",    "v",    "v",    "v"],
        ["v",    "v",    "m00m3","m00m3","m00m5","e02e1","b00b3","m00m3","m00m3","v",    "v"],
        ["v",    "m00m3","e12e1","b00b3","b00b3","m00m5","b00b3","b00b3","e22e1","m00m3","v"],
        ["v",    "m00m3","m00m5","m00m5","b00b3","m00m5","b00b3","m00m5","m00m5","m00m3","v"],
        ["m00m3","m00m5","b00b3","b00b3","b00b3","p00p3","b00b3","m00m5","b00b3","e32e1","m00m3"],
        ["m00m3","e42e1","b00b3","m00m5","b00b3","b00b3","b00b3","b00b3","b00b3","m00m5","m00m3"],
        ["v",    "m00m3","m00m5","m00m5","b00b3","m00m5","b00b3","m00m5","m00m5","m00m3","v"],
        ["v",    "m00m3","e52e1","b00b3","b00b3","m00m5","b00b3","b00b3","e62e1","m00m3","v"],
        ["v",    "v",    "m00m3","m00m3","b00b3","e72e1","m00m5","m00m3","m00m3","v",    "v"],
        ["v",    "v",    "v",    "v",    "m00m3","m00m3","m00m3","v",    "v",    "v",    "v"]])]