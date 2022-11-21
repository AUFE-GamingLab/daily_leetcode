for dir in `ls`
do
	if [ -d $dir ];then
		echo $dir;
		for problem_dir in `ls ${dir}` 
		do
			base_problem_dir="${dir}${problem_dir}";
			if [ -d  ${base_problem_dir} ];then
				echo "${problem_dir:0:-1}"
				current_dir=`ls ${base_problem_dir}`
				for p_dir in $current_dir
				do
					if [ -d "${base_problem_dir}${p_dir}" ];then
					echo "   ${p_dir:0:-1}"
					fi
				done
			fi
		done
	fi
done
