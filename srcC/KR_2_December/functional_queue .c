#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct ListNode {
    int value;
    struct ListNode *next;
} ListNode;

ListNode *list_cons(int value, ListNode *next) {
    ListNode *node = (ListNode*)malloc(sizeof(ListNode));
    if (node == NULL) {
        fprintf(stderr, "Out of memory\n");
        exit(EXIT_FAILURE);
    }
    node->value = value;
    node->next = next;
    return node;
}

ListNode *list_reverse(ListNode *xs) {
    ListNode *acc = NULL;
    while (xs != NULL) {
        acc = list_cons(xs->value, acc);
        xs = xs->next;
    }
    return acc;
}

typedef struct {
    ListNode *front;
    ListNode *rear;
} Queue;

typedef struct {
    int ok;
    int value;
    Queue queue;
} DequeueResult;

Queue queue_normalize(Queue q) {
    if (q.front == NULL && q.rear != NULL) {
        q.front = list_reverse(q.rear);
        q.rear = NULL;
    }
    return q;
}

Queue queue_empty(void) {
    Queue q;
    q.front = NULL;
    q.rear = NULL;
    return q;
}

int queue_is_empty(Queue q) {
    if (q.front == NULL) {
        return 1;
    } else {
        return 0;
    }
}

Queue enqueue(Queue q, int x) {
    Queue newq;
    newq.front = q.front;
    newq.rear = list_cons(x, q.rear);
    newq = queue_normalize(newq);
    return newq;
}

DequeueResult dequeue(Queue q) {
    DequeueResult res;
    if (queue_is_empty(q)) {
        res.ok = 0;
        return res;
    }

    ListNode *old_front = q.front;
    int value = old_front->value;

    Queue newq;
    newq.front = old_front->next;
    newq.rear = q.rear;
    newq = queue_normalize(newq);
    res.ok = 1;
    res.value = value;
    res.queue = newq;
    return res;
}



void test_empty_queue(void) {

    Queue q = queue_empty();
    assert(queue_is_empty(q));

    // вытягваем элемент из очереди
    DequeueResult r = dequeue(q);
    assert(r.ok == 0);
}

void test_simple_enqueue_dequeue(void) {
    Queue q = queue_empty();
    q = enqueue(q, 1);
    q = enqueue(q, 2);
    q = enqueue(q, 3);

    assert(!queue_is_empty(q));

    DequeueResult r1 = dequeue(q);
    assert(r1.ok == 1 && r1.value == 1);

    DequeueResult r2 = dequeue(r1.queue);
    assert(r2.ok == 1 && r2.value == 2);

    DequeueResult r3 = dequeue(r2.queue);
    assert(r3.ok == 1 && r3.value == 3);

    // после всех извлечей очередь должна быть пустой
    assert(queue_is_empty(r3.queue));
}

void test_interleaving(void) {
    Queue q0 = queue_empty();
    Queue q1 = enqueue(q0, 10);
    Queue q2 = enqueue(q1, 20);
    Queue q3 = enqueue(q2, 30);

    // выбераем первый элемент
    DequeueResult r1 = dequeue(q3);
    assert(r1.ok == 1 && r1.value == 10);
    Queue q4 = enqueue(r1.queue, 40);
    Queue q5 = enqueue(q4, 50);

    int expected[] = {20, 30, 40, 50};
    int n = sizeof(expected) / sizeof(expected[0]);

    Queue q = q5;
    int i = 0;
    // вынимаем все элементы и сравниваем с expected
    while (i < n) {
        DequeueResult r = dequeue(q);
        assert(r.ok == 1);
        assert(r.value == expected[i]);
        q = r.queue;
        i++;
    }
    assert(queue_is_empty(q));
}

void test_persistence(void) {
    //строим цепочку состояний
    Queue q0 = queue_empty();
    Queue q1 = enqueue(q0, 1);
    Queue q2 = enqueue(q1, 2);
    Queue q3 = enqueue(q2, 3);

    // выбираем первый элемент из состояния q3 
    DequeueResult r = dequeue(q3);
    assert(r.ok == 1 && r.value == 1);
    DequeueResult r_again = dequeue(q3);
    assert(r_again.ok == 1 && r_again.value == 1);
    DequeueResult r2 = dequeue(q2);
    assert(r2.ok == 1 && r2.value == 1);
}

int main(void) {
    test_empty_queue();
    test_simple_enqueue_dequeue();
    test_interleaving();
    test_persistence();
    printf("Тесты пройдены\n");
    return 0;
}