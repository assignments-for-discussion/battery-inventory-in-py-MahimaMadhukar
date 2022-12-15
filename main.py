
def count_batteries_by_usage(cycles):
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] <=310)
  assert(counts["mediumCount"] >310 and <=929)
  assert(counts["highCount"] >=930)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
  
