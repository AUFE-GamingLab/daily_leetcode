for dir in `ls`
do
	if [ -d $dir ];then
		echo $dir;
		for problem_dir in `ls ${dir}` 
		do
			echo "初始化 ${dir}${problem_dir}";
			init_file_name="init__.sh"
			touch "${dir}${problem_dir}${init_file_name}"
		done
	fi
done
