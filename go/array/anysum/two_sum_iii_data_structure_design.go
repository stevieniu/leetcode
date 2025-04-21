package anysum

import "sort"

type TwoSum struct {
	nums      []int
	is_sorted bool
}

func Constructor() TwoSum {
	return TwoSum{nums: []int{}, is_sorted: false}
}

func (this *TwoSum) Add(number int) {
	this.nums = append(this.nums, number)
	this.is_sorted = false
}

func (this *TwoSum) Find(value int) bool {
	if !this.is_sorted {
		sort.Ints(this.nums)
		this.is_sorted = true
	}
	l, r := 0, len(this.nums)-1
	for l < r {
		sum := this.nums[l] + this.nums[r]
		if sum == value {
			return true
		} else if sum > value {
			r--
		} else {
			l++
		}
	}
	return false
}

/**
 * Your TwoSum object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(number);
 * param_2 := obj.Find(value);
 */
