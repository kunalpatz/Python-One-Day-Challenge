import sys

landscape_paintings = {}
portrait_paintings = {}
frames = {}
temp_frame=[]

input_file = open(sys.argv[1], "r")
submit_file = open("submit_"+sys.argv[1], "w")


input_list = input_file.readlines()

# Count of paintings in given file
nos_data = int(input_list[0])


for i in range(1, nos_data+1):
    data = input_list[i].strip('\n').split(' ')
    if data[0] == 'P':
        temp_frame.append({str(i-1): [data[1], data[2:]]}) # appending data to temp frame
        if len(temp_frame) == 2: # checking if length of temp frame is 2 or not in case of portraits
            tag =[]
            keys = []
            for portrait in temp_frame:
                for k, v in portrait.items():
                    tag.append(v[1]) # append tags
                    keys.append(k)
            common_tags = list(set(tag[0]).union(set(tag[1]))) #merging two lists of tags of portraits to eliminate duplicate
            common_tags.insert(0, str(len(common_tags)))
            frames.update({str(keys[0])+' '+str(keys[1]): common_tags})
            temp_frame = []
        continue
    else:
        tags = data[2:]
        tags.insert(0, data[1])
        frames.update({str(i-1): tags})


def based_on_tagSize(frames):
    tag_size = {}
    submit_file.write(str(len(frames))+"\n")
    for frame in frames:
        if frames[frame][0] in tag_size.keys():
            tag_size[frames[frame][0]].append(frame)
        else:
            tag_size[frames[frame][0]] = [frame]
    tag_size_list = list(tag_size.keys())
    intermediate_sorted_list = sorted([int(x) for x in tag_size_list])
    list_with_stringdata = [str(x) for x in intermediate_sorted_list]
    for i in list_with_stringdata:
        for size in tag_size[i]:
            submit_file.write(str(size)+"\n")
    submit_file.close()

based_on_tagSize(frames)

