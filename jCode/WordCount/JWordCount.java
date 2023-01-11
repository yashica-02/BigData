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

public class JWordCount{
    public static void main(String[] args) throws IOException{
        Configuration c = new Configuration();
        
        Job job = new Job(c, "jwordcount");
        
        job.setJar("JWC.jar");
        job.setJarByClass(JWordCount.class);
        
        job.setMapperClass(MapWC.class);
        job.setReducerClass(ReduceWC.class);
        
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0:1);
    }
}


public static class MapWC extends Mapper<LongWritable, Text, Text, IntWritable> {
    protected void map(LongWritable key, Text value, Context con) throws IOException, InterruptedException{
        String line = value.toString(); //convert hadoop text(value) into Java String(line)
        String[] words = line.split(",");   //add into list "words" after splitting
        for (String word: words){
            Text outputKey = new Text(word.toUpperCase().trim());   //convert into haddop readable Text
            IntWritable outputValue = new IntWritable(1);   //int=1; converted into Hadoop data type
            con.write(outputKey, outputValue);
        }
    }
}



public class ReduceWC extends Reducer<Text, IntWritable, Text, IntWritable> {
    protected void reduce(Text words, Iterable<IntWritable> values, Context con) throws IOException, InterruptedException{
        int sum =0;
        for(IntWritable value : values){
            sum += value.get(); //convert value from IntWritable to int and then increment sum
        }
        con.write(word, new IntWritable(sum));
    }
}