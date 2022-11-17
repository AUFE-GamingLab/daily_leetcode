for dir in `ls`
do
	if [ -d $dir ];then
		echo $dir;
		for problem_dir in `ls ${dir}` 
		do
			base_problem_dir="${dir}${problem_dir}";
			if [ -d  ${base_problem_dir} ];then
				echo "初始化 ${base_problem_dir}";
				init_file_name="init__.sh"
				target_file="${base_problem_dir}${init_file_name}";
				if [ -e $target_file ];then	
					echo "${target_file}已经初始化";
				else
					touch $target_file;
				fi
			fi
		done
	fi
done
