def fix_size(sizes: tuple, pix: int=512) -> tuple:
    def fix(size, pix):
        size = pix - size
        if size != 0:
            return size//2
        return size
    return tuple(fix(size, pix) for size in sizes)
