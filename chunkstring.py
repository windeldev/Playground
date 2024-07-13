import sys

#          1         2         3         4         5         6         7         8         9         0
#01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
#"24071214, 24071215, 24071216, 24071217, 24071218, 24071219, 24071220, 24071221, 24071222, 24071223"
#"thisisaverylongsentence. letsseehowthechunkwillhappen! resultswillnowbehere"
#"thisisaverylongsentence.letsseehowthechunkwillhappen!resultswillnowbehere"
#"the quick brown fox jumped over the lazy dog"
#" .,;.....,,,,,;;;;      ....!!!!! .,;.....,,,,,;;;;      ....!!!!! .,;.....,,,,,;;;;      ....!!!!!"
#"test string"
#" "
#""
def chunkstring(txt, limit, delims = [' ', '.', ',', '?', '!', ';', '\n', '\t']):
	start = 0
	chunks = []
	txt_size = len(txt)
	while start < txt_size:
		end = start + limit
		if end >= txt_size: end = txt_size
		else:
			piece = txt[start:end]
			found_delims = [ piece.rfind(d) for d in delims if d in piece]
			if found_delims and piece[-1] not in delims and piece[0] not in delims:
				end = max(found_delims) + start
		chunks.append(txt[start:end])
		start = end
	return chunks

if len(sys.argv) > 1:
	print(chunkstring(sys.argv[1], 20))
else:
	#itxt = input("Enter a string to chunk: ")
	#ilimit = input("Enter a size to chunk: ")
	#chunkstring(itxt, int(ilimit))
	print(chunkstring("24071214, 24071215, 24071216, 24071217, 24071218, 24071219, 24071220, 24071221, 24071222, 24071223", 20) or "Empty string")
	print(chunkstring("thisisaverylongsentence. letsseehowthechunkwillhappen! resultswillnowbehere", 20) or "Empty string")
	print(chunkstring("thisisaverylongsentence.letsseehowthechunkwillhappen!resultswillnowbehere", 20) or "Empty string")
	print(chunkstring("the quick brown fox jumped over the lazy dog", 20) or "Empty string")
	print(chunkstring(" .,;.....,,,,,;;;;      ....!!!!! .,;....,;.....,,,,,;;;;      ....!!!!!", 20) or "Empty string")
	print(chunkstring("test string", 20) or "Empty string")
	print(chunkstring(" ", 20) or "Empty string")
	print(chunkstring("", 20) or "Empty string")


"""
	def chunkstring(txt, limit):
		delims = [' ', '.', ',', ';', '\n', '\t']
		start = 0
		chunks = []
		txt_size = len(txt)
		while start < txt_size:
			end = start + limit
			if end > txt_size:
				end = txt_size
			else:
				_end = end
				while start < _end and txt[_end - 1] not in delims:
					_end -= 1
				if _end > start:
					end = _end
			chunks.append(txt[start:end])
			start = end
		return chunks
"""
