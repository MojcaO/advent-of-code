package is.mojca.aoc2023;

import java.net.URLConnection;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URL;
import java.nio.channels.Channels;
import java.nio.channels.ReadableByteChannel;

public class ReadInput {
    public static String[] readInput(int day) throws IOException {

        String path = System.getProperty("user.dir")+"\\input\\"+day+".txt";

        List<String> listOfStrings;
        listOfStrings = Files.readAllLines(Path.of(path));

        // convert arraylist to array
        String[] input = listOfStrings.toArray(new String[0]);

        return input;
    }
}
