import java.util.Arrays;
import java.util.LinkedList;

public class Test {
    public static void main(String[] args) {
        int num= 9973;
        new Test().maximumSwap(num);
    }

    public int maximumSwap(int num) {
        LinkedList<Integer> q = new LinkedList<>();
        while(num != 0) {
            q.addFirst(num % 10);
            num /= 10;
        }

        int[] maxIdToRight = new int[q.size()];
        Arrays.fill(maxIdToRight, q.size() - 1);

        int maxSeen = -1, maxSeenAt = q.size();
        for(int i = q.size() - 1; i >= 0; i--) {
            int cur = q.get(i);
            maxIdToRight[i] = maxSeenAt;
            if (maxSeen < cur) {
                maxSeen = cur;
                maxSeenAt = i;
            }
        }

        for (int i = 0; i < maxIdToRight.length; i++) {
            if(q.get(i) < q.get(maxIdToRight[i])) {
                int tmp = q.get(i);
                q.set(i, q.get(maxIdToRight[i]));
                q.set(maxIdToRight[i], tmp);
                break;
            }
        }
        int ans = 0;
        for(int i = 0; i < q.size(); i ++) {
            ans = 10 * ans + q.get(i);
        }
        return ans;
    }
}
