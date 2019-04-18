def rubydiff(snap_before, snap_after) -> str:
    snap_before = snap_before if snap_before is not None else {}
    snap_after = snap_after if snap_after is not None else {}

    txt = []
    for key in sorted(set().union(
            snap_before,
            snap_after
    )):
        old = snap_before.get(key)
        new = snap_after.get(key)

        old = old if old is not None else ""
        new = new if new is not None else ""

        if old != new:
            txt += ["{}:\n- {}\n- {}\n".format(key, old, new)]

    return "".join(txt)
