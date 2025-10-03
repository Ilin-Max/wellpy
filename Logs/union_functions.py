import numpy as np

def converе_to_numpy_array(array):
    # np_array = np.array([array])
    
    # if type(array) != type(np_array) and len(array) != 0:
    #     try:
    #         np_array = np.array(array)
    #     except Exception as e:
    #         print(e)

    return np.array([array])

def sort_arrays_by_index(index_array, source_array):
    sort_idx = np.argsort(index_array)
    sorted_idx = index_array[sort_idx]
    sorted_array = source_array[sort_idx]
    
    return sorted_idx, sorted_array

def delete_nan(index_array, source_array):
    valid_mask = ~np.isnan(source_array)
    index_clean = index_array[valid_mask]
    curve_clean = source_array[valid_mask]
    return  index_clean, curve_clean


def linear_interpolation(main_index_array, source_index_array, source_array, nan_value = np.nan, win_search = 0):
    # main_index_array = converе_to_numpy_array(main_index_array)
    interpolated_array = np.zeros_like(main_index_array)

    # source_index_array = converе_to_numpy_array(source_index_array)
    # source_array = converе_to_numpy_array(source_array)
    source_index_array, source_array = delete_nan(source_index_array, source_array)
    source_index_array, source_array = sort_arrays_by_index(source_index_array, source_array)
    
    if win_search == 0:
        interpolated_array = np.interp(
            main_index_array,
            source_index_array,
            source_array,
            left=nan_value,
            right=nan_value
        )
    
    else:
        # Находим сегменты с учетом окна поиска
        gaps = np.diff(source_index_array)
        large_gap_indices = np.where(gaps > win_search)[0]
        
        # Границы сегментов
        segment_boundaries = [0] + list(large_gap_indices + 1) + [len(source_index_array)]
        segments = []
        
        for i in range(len(segment_boundaries) - 1):
            start = segment_boundaries[i]
            end = segment_boundaries[i + 1] - 1
            if end >= start:  # Проверяем, что сегмент не пустой
                segments.append((start, end))
        
        # Интерполируем по сегментам
        for start_idx, end_idx in segments:
            seg_depths = source_index_array[start_idx:end_idx + 1]
            seg_measurements = source_array[start_idx:end_idx + 1]
            
            if len(seg_depths) < 2:
                continue
                
            # Находим целевые точки внутри сегмента
            mask = (main_index_array >= seg_depths[0]) & (main_index_array <= seg_depths[-1])
            
            if np.any(mask):
                interpolated_array[mask] = np.interp(
                    main_index_array[mask], seg_depths, seg_measurements,
                    left=nan_value, right=nan_value
            )
    
    return interpolated_array


