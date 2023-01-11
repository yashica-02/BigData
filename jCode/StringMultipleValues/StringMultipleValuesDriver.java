import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.util.GenericOptionsParser;

public class StringMultipleValuesDriver {

	public static void main(String[] args) throws Exception {

		Configuration conf = new Configuration();
		String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
		
		if (otherArgs.length != 2) {
		  System.err.println("Usage: StringMultipleValuesDriver <in> <out>");
		  System.exit(2);
		}
		
		Job job = Job.getInstance(conf, "String multiple values");
		job.setJar("multiple.jar");
        job.setJarByClass(StringMultipleValuesDriver.class);
        job.setJobName("Multiple");
        
		FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
		
        job.setMapperClass(StringMultipleValuesMapper.class);
        job.setReducerClass(StringMultipleValuesReducer.class);
        
		job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);
        
		System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
}