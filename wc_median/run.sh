cd wc_input
cat * | tr [\\n,.\"\] ' ' > tempFile.txt
python ../wc.py tempFile.txt
mv wc_result.txt ../wc_output

cat * | awk -F ' ' '{print NF}' > tempFile.txt
python ../wm.py tempFile.txt
mv med_result.txt ../wc_output
rm tempFile.txt