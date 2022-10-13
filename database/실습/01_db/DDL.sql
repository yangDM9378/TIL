-- 실습코드 작성
-- 마우스 오른쪽 버튼->Use Database로 데이터 베이스 연결
-- 실행하고자하는 문장안에서 오른쪽 버튼 run Query(전체 문장 실행)
-- 실행하고자하는 문장안에서 오른쪽 버튼 run selected Query(해당문장)
CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTERGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);

-- Alter Table
-- Rename a table(테이블 이름 변경)
ALTER TABLE contacts RENAME TO new_contacts;
-- Rename a column(컬럼명 변경)
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;
-- Add a new column to a table(새 컬럼 추가)
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;
-- DELETE a column(컬럼 삭제)
ALTER TABLE new_contacts DROP COLUMN address;

-- DROP Table
DROP TABLE new_contacts;
DROP TABLE contacts;```