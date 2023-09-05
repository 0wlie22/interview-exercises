"""
You've built an inflight entertainment system with on-demand movie streaming.
Users on longer flights like to start a second movie right when their first one ends,
but they complain that the plane usually lands before they can see the ending.
So you're building a feature for choosing two movies whose total runtimes will equal
the exact flight length.
"""


def is_sum(flight_length: int, movie_lengths: list[int]) -> bool:
    """
    Given a flight length (in minutes) and a list of movie lengths (in minutes),
    return True if there exists a pair of movies that add up exactly to the flight length.
    """
    for i in range(len(movie_lengths)):
        if flight_length - movie_lengths[i] in movie_lengths[i + 1 :]:
            return True

    return False


def main():
    flight_length = 120
    movie_lengths = [30, 60, 60]
    print(is_sum(flight_length, movie_lengths))


if __name__ == "__main__":
    main()
