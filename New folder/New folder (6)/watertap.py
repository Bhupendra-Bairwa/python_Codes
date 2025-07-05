def trap_rain_water(arr):
    n = len(arr)
    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    water_trapped = 0

    while left < right:
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water_trapped += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water_trapped += right_max - arr[right]
            right -= 1

    return water_trapped
