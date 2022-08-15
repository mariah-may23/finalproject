import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600

FONT_BIG = pygame.font.SysFont('comicsans', 40)
FONT_MEDIUM = pygame.font.SysFont('comicsans', 30)
FONT_SMALL = pygame.font.SysFont('comicsans', 20)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sorting Algorithm Visualizer')

DARK_GRAY = '#65696B'
LIGHT_GRAY = '#C4C5BF'
BLUE = '#0CA8F6'
DARK_BLUE = '#4204CC'
WHITE = '#FFFFFF'
BLACK = '#000000'
RED = '#F22810'
YELLOW = '#F7E806'
PINK = '#F50BED'
GREEN = '#013220'
PURPLE = '#BF01FB'

NUM_BAR = 170
BORDER = 25

SORTED = False

SPACE = (WIDTH - 25 - BORDER) / NUM_BAR

BAR_WIDTH, BAR_HEIGHT = SPACE - 1.2, 2.87

FPS = 80

RUN = True

DOWN = 25

COUNT = 0

sorting = [FONT_SMALL.render('M - Merge Sort', 1, RED),
           FONT_SMALL.render('B - Bubble Sort', 1, RED),
           FONT_SMALL.render('Q - Quick Sort', 1, RED),
           FONT_SMALL.render('I - Insertion Sort', 1, RED)]
reset = FONT_SMALL.render('R - Reset', 1, RED)


class Bar:

    def __init__(self, x, y, width, height, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = BLACK
        self.value = value

    def reset(self, num):
        self.x = BORDER + num * SPACE
        return self

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def check(self):
        self.color = RED

    def done(self):
        self.color = BLUE

    def match(self):
        self.color = YELLOW

    def back(self):
        self.color = BLUE


sort = [x for x in range(1, NUM_BAR + 2)]
random.shuffle(sort)
bar = [Bar((BORDER + i * SPACE), (HEIGHT - DOWN - (BAR_HEIGHT * sort[i])), BAR_WIDTH, BAR_HEIGHT * sort[i], sort[i]) for
       i in range(NUM_BAR)]


def main(win):
    clock = pygame.time.Clock()

    global RUN
    global bar
    global SORTED
    while RUN:

        clock.tick(FPS)
        draw(win, bar)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            random.shuffle(sort)
            bar = [Bar((BORDER + i * SPACE), (HEIGHT - DOWN - (BAR_HEIGHT * sort[i])), BAR_WIDTH, BAR_HEIGHT * sort[i],
                       sort[i]) for i in range(NUM_BAR)]
            SORTED = False
        if keys[pygame.K_s]:
            check()
            selection(bar, win)
        if keys[pygame.K_b]:
            check()
            bubble(bar, win)
        if keys[pygame.K_m]:
            check()
            merge_sort(bar, 0, len(bar) - 1, win)
        if keys[pygame.K_q]:
            check()
            quick_sort(bar, 0, len(bar) - 1, win)

        if keys[pygame.K_i]:
            check()
            insertion(bar, win)

    pygame.quit()


def check():
    global SORTED
    global bar
    if SORTED:
        SORTED = False
        random.shuffle(sort)
        bar = [Bar((BORDER + i * SPACE), (HEIGHT - DOWN - (BAR_HEIGHT * sort[i])), BAR_WIDTH, BAR_HEIGHT * sort[i],
                   sort[i]) for i in range(NUM_BAR)]


# draw function for the screen
def draw(win, bar):
    global reset
    global sorting

    win.fill(WHITE)

    pygame.draw.rect(win, WHITE, (0, 0, 800, 180))

    x = 45
    y = 15
    win.blit(sorting[0], (x, y))
    x = x + 180
    win.blit(sorting[1], (x, y))
    x = x + 180
    win.blit(sorting[2], (x, y))
    x = x + 180
    win.blit(sorting[3], (x, y))

    win.blit(reset, (330, 45))

    for i in bar:
        i.draw(win)

    pygame.display.update()





def bubble(bar, win):
    global RUN
    global SORTED
    SORTED = True

    for i in range(len(bar)):
        if not RUN:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break

        for j in range(len(bar) - 1 - i):

            bar[j].check()
            draw(win, bar)
            bar[j].back()

            if bar[j].value > bar[j + 1].value:
                temp = bar[j]
                bar[j] = bar[j + 1]
                bar[j + 1] = temp
                bar[j].reset(j)
                bar[j + 1].reset(j + 1)

        bar[len(bar) - 1 - i].done()


def merge(bar, left, mid, right, win):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        bar[i].check()
        bar[j].check()
        draw(win, bar)
        bar[i].back()
        bar[j].back()
        if bar[i].value < bar[j].value:
            temp.append(bar[i])
            i += 1
        else:
            temp.append(bar[j])
            j += 1
    while i <= mid:
        bar[i].check()
        draw(win, bar)
        bar[i].back()
        temp.append(bar[i])
        i += 1
    while j <= right:
        bar[j].check()
        draw(win, bar)
        bar[j].back()
        temp.append(bar[j])
        j += 1
    k = 0
    for i in range(left, right + 1):
        bar[i] = temp[k]
        bar[i].reset(i)
        bar[i].check()
        draw(win, bar)
        if right - left == len(bar) - 1:
            bar[i].done()
        else:
            bar[i].back()
        k += 1


def merge_sort(bar, left, right, win):
    global SORTED
    SORTED = True
    global RUN

    mid = left + (right - left) // 2
    if left < right:
        merge_sort(bar, left, mid, win)
        merge_sort(bar, mid + 1, right, win)
        if not RUN:
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break
        merge(bar, left, mid, right, win)


def quick_sort(bar, low, high, win):
    global RUN
    global SORTED
    SORTED = True

    if len(bar) == 1:
        return bar
    if low < high:

        pi = partition(bar, low, high, win)

        draw(win, bar)

        quick_sort(bar, low, pi - 1, win)

        if not RUN:
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break

        for i in range(pi + 1):
            bar[i].done()

        quick_sort(bar, pi, high, win)


def partition(bar, low, high, win):
    i = low
    pivot = bar[high]
    pivot.color = RED
    for j in range(low, high):

        bar[j].check()
        bar[i].check()
        draw(win, bar)
        bar[j].back()
        bar[i].back()
        if bar[j].value < pivot.value:
            bar[i], bar[j] = bar[j], bar[i]
            bar[i].reset(i)
            bar[j].reset(j)
            i += 1

    bar[i], bar[high] = bar[high], bar[i]
    bar[i].reset(i)
    pivot.back()
    draw(win, bar)
    bar[high].reset(high)
    return i


def insertion(bar, win):
    global RUN
    global SORTED
    SORTED = True

    for i in range(1, len(bar)):
        bar[i].check()
        draw(win, bar)
        bar[i].back()
        j = i
        while j > 0 and bar[j].value < bar[j - 1].value:
            if not RUN:
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
                    break
            bar[i].check()
            draw(win, bar)
            bar[i].back()
            bar[j], bar[j - 1] = bar[j - 1], bar[j]
            bar[j].reset(j)
            bar[j - 1].reset(j - 1)
            j -= 1
    for i in range(len(bar)):
        bar[i].done()
        pygame.time.delay(1)
        draw(win, bar)


if __name__ == "__main__":
    main(win)
