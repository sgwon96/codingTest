package greedy;

import java.util.*;

class Edge implements Comparable<Edge>{

    private int nodeA;
    private int nodeB;
    private int distance;

    public Edge(int nodeA, int nodeB, int distance) {
        this.nodeA = nodeA;
        this.nodeB = nodeB;
        this.distance = distance;
    }

    public int getNodeA() {
        return nodeA;
    }

    public int getNodeB() {
        return nodeB;
    }

    public int getDistance() {
        return distance;
    }

    @Override
    public int compareTo(Edge o) {
        if (this.distance < o.distance)
            return -1;
        else
            return 1;
    }
}

class 섬연결하기 {

    public static int[] parent = new int[10001];

    // 모든 간선을 담을 그래프 edges 최종 비용 cost 선언
    public static ArrayList<Edge> edges = new ArrayList<>();

    // 특정 원소의 부모 노드 찾기
    public static int findParent(int x){
        if (parent[x] == x)
            return x;
        else
            return parent[x] = findParent(parent[x]);
    }

    // 두 원소가 속한 집합을 합치기
    public static void unionParent(int a, int b){
        a = parent[a];
        b = parent[b];
        if (a < b)
            parent[b] = a;
        else
            parent[a] = b;
    }

    public int solution(int n, int[][] costs) {
        int result = 0;

        // 부모 테이블상에서, 부모를 자기 자신으로 초기화
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        // 모든 간선에 대한 정보 입력
        for (int i = 0; i < costs.length ; i++){
            edges.add(new Edge(costs[i][0],costs[i][1],costs[i][2]));
        }

        // 간선을 비용순으로 정렬
        Collections.sort(edges);

        // 간선을 하나씩 확인하며
        for (int i = 0; i < edges.size(); i++) {
            int cost = edges.get(i).getDistance();
            int a = edges.get(i).getNodeA();
            int b = edges.get(i).getNodeB();
            // 사이클이 발생하지 않는 경우에만 집합에 포함
            if (findParent(a) != findParent(b)) {
                unionParent(a, b);
                result += cost;
            }
        }

        return result;
    }
}