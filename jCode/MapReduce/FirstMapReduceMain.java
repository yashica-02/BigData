import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class FirstMapReduceMain{
    public static void main(String[] args) throws Exception{
        if(args.length!=2){
            System.err.println("Usage: FirstMapReduceMain <input path> <output path>");
            System.exit(-1);
        }
        Job job = Job.getInstance();
        
        job.setJarByClass(FirstMapReduceMain.class);    //specify the main class
        job.setJar("FMR.jar");  //specify the jar file
        job.setJobName("FirstMapReduceMain");   //dummy name; used for debugging purpose
        
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        job.setMapperClass(FirstMapReduceMapper.class);
        job.setReducerClass(FirstMapReduceReducer.class);

        job.setOutputKeyClass(LongWritable.class); //mapper output key data type
        job.setOutputValueClass(Text.class); //reducer output key data type

        System.exit(job.waitForCompletion(true) ? 0:1); //if success then 0 else 1
    }
}