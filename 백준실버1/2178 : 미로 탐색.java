// sliver 1 1번
//참고 : https://wonit.tistory.com/421, https://velog.io/@lifeisbeautiful/Java-%EB%B0%B1%EC%A4%80-2178%EB%B2%88-%EB%AF%B8%EB%A1%9C-%ED%83%90%EC%83%89-%EC%9E%90%EB%B0%94
package back_sliver1;

import java.util.*;
import java.util.Queue;

public class miro {

    static boolean visit[][]; //bfs같은 문제는 무조건 visit 만들기
    static int dirY[] = {-1, 1, 0, 0};
    static int dirX[] = {0, 0, -1, 1};
    static Queue<Node> que = new LinkedList<>(); //큐를 사용하기 위한 자료구조
    //Node는 maze point

    static int now_x, now_y; //현재 위치한 노드를 저장하기 위한 변수
    static int x, y;

    static class Node {
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static int solution(int col, int row, int[][] maze) throws Exception {

        int answer = 0;

        visit = new boolean[col][row]; //col, row값 만큼 방문확인 배열 초기화 true로 초기화 되는 듯

        BFS(0, 0, col, row, maze); //col, row, maze값을 모두 들고가 bfs 실행
        answer = maze[col-1][row-1];
        return answer;
    }

    static void BFS(int x, int y, int col, int row, int[][] maze) {
        que.offer(new Node(x, y));
        visit[y][x] = true;

        while(!que.isEmpty()) {
            Node node = que.poll();

            for(int i=0; i<4; i++) {
                now_y = node.y + dirY[i];
                now_x = node.x + dirX[i];

                if(Range_check(col, row) == true && visit[now_y][now_x] == false && maze[now_y][now_x] == 1) {
                    que.offer(new Node(now_x, now_y));
					visit[now_y][now_x] = true;	

					maze[now_y][now_x] = maze[node.y][node.x] + 1;
					if(visit[col-1][row-1] == true) {
						return;
					}
                }
            }
        }
    }

    public static boolean Range_check(int col, int row) {
        return (now_x >= 0 && now_x < row && now_y >= 0 && now_y < col);
    }

    public static void main(String[] args) throws Exception {
        System.out.println(solution(4, 6, new int[][]{{1,0,1,1,1,1},{1,0,1,0,1,0},{1,0,1,0,1,1},{1,1,1,0,1,1}}));
    }
}

//테스트케이스는 맞았는데 틀렸다고 한다 킹받...:(
