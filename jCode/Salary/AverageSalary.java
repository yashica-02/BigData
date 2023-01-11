import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class AverageSalary{
    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException{
        Configuration c = new Configuration();
        String[] otherArgs = new GenericOptionsParser(c, args).getRemainingArgs();
        if(otherArgs.length!=2){
            System.err.println("Number of arguments passed is not 2");
            System.exit(1);
        }

        Job job = Job.getInstance(c, "word count");
        job.setJar("avgsal.jar");

        job.setJarByClass(AverageSalary.class);
        job.setMapperClass(Map.class);
        job.setReducerClass(Reduce.class);
        
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0:1);
    }


    public static class Map extends Mapper<LongWritable, Text, Text, IntWritable> {
        Text outKey = new Text();
        IntWritable outValue = new IntWritable();
        
        protected void map(LongWritable key, Text value, Context con) throws IOException, InterruptedException{
            String[] colmn = value.toString().split(",");
            outKey.set(colmn[2]);
            outValue.set(Integer.parseInt(colmn[3]));
            con.write(outKey, outValue);
        }
    }



    public class Reduce extends Reducer<Text, IntWritable, Text, IntWritable> {
        IntWritable outValue = new IntWritable();

        protected void reduce(Text key, Iterable<IntWritable> value, Context con) throws IOException, InterruptedException{
            int sum =0; int count = 0; int avg;
            for(IntWritable sal:value){
                sum = sum + sal.get();
                count++;
            }
            avg = sum/count;
            outValue.set(avg);
            con.write(key, outValue);
        }
    }
}